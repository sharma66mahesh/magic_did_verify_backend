import json
import base64
from eth_account.messages import encode_defunct
from web3.auto import w3
import logging

log_level = logging.DEBUG
# log_level = logging.INFO
logging.basicConfig(format="%(message)s", level=logging.DEBUG)


def generate_public_key(claim: dict) -> str:
    """
    Generates public key from claim

    Sample claim:{"iat":1629353792,"ext":1629354692,"iss":"did:ethr:0xC363a0c816652Fae5401c77645AED2b4f77eC7e9","sub":"NIx6CVVaM0Dpqp0IvrkkzX5f2Vub20OiFt-dEEq01q8=","aud":"RHa65uclcbZyMN7GUVkdfGtD69MrRThUOsidvtsKxK0=","nbf":1629353792,"tid":"7b00ecdd-385b-46f3-a364-bc40c78b2149","add":"0x0bfd8b6d9c83e4018b6209f528f0e98f7f796ae45d93d0c7e405db8696c64190109b011d0733f2973ed6c9e35ffb4e3c63d610ae3448f70231bbed3b52d829f41c"}
    :param claim:
    :return:
    """
    return claim['iss'].split(':')[2]


def generate_signing_key(claim_string: str, proof: str) -> str:
    """
    Generates signing key from claim string and proof
    :param claim_string:
    :param proof:
    :return:
    """
    # create hash of claim_string
    hashed_claim = encode_defunct(text=claim_string)
    # TODO: remove hash or use different hashing
    return w3.eth.account.recover_message(hashed_claim, signature=proof)


def decode_did(req_body: dict) -> None:
    logging.debug(f"req_body: {req_body}")
    did_token, additional_claim = req_body['idToken'], req_body['additionalData']
    logging.debug(f"did_token: {did_token}")
    logging.debug(f"additional_claim: {additional_claim}")

    # decode the didToken
    message = json.loads(base64.b64decode(did_token).decode('utf-8'))
    # separate out proof and claim
    proof, claim_string = message[0], message[1]

    claim = json.loads(claim_string)
    # SAMPLE of claim:
    # 0x66393f88f36b06bf5741cfd14bdcde8a0a6eb954a85df57a7612b56dba7186a2704ceb4600ced841d911f147ee8849da54ca7841c46b05b592b09eb6a73ec3831b

    public_key = generate_public_key(claim)
    logging.debug(f"public_key: {public_key}")
    signing_public_key = generate_signing_key(claim_string, proof)
    logging.debug(f"signing_public_key: {signing_public_key}")

    if signing_public_key != public_key:
        raise Exception('Could not verify the identity of the user')

    # Now verify that email and walletAddress sent are authentic too
    hashed_additional_claim = encode_defunct(text=additional_claim)
    additional_signing_public_key = w3.eth.account.recover_message(hashed_additional_claim,
                                                                   signature=claim['add'])
    if additional_signing_public_key != public_key:
        raise Exception('Could not verify email and walletAddress')
