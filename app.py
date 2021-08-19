from flask import Flask, request, jsonify
from flask_cors import CORS
import json
import base64
from eth_account.messages import encode_defunct
from web3.auto import w3
import traceback

app = Flask(__name__)
CORS(app)


@app.route('/', methods=['POST'])
def decodeDidToken():
  try: 
    # parse didToken from request
    req_body = request.get_json()
    did_token = req_body['idToken']
    additional_data_string = req_body['additionalData']  # email and walletAddress
    additional_data = json.loads(additional_data_string)

    # decode the didToken
    message = json.loads(base64.b64decode(did_token).decode('utf-8'))

    # separate out proof and claim
    proof = message[0] # SAMPLE: 0x66393f88f36b06bf5741cfd14bdcde8a0a6eb954a85df57a7612b56dba7186a2704ceb4600ced841d911f147ee8849da54ca7841c46b05b592b09eb6a73ec3831b
    claim_string = message[1]
    claim = json.loads(claim_string) # SAMPLE: {"iat":1629353792,"ext":1629354692,"iss":"did:ethr:0xC363a0c816652Fae5401c77645AED2b4f77eC7e9","sub":"NIx6CVVaM0Dpqp0IvrkkzX5f2Vub20OiFt-dEEq01q8=","aud":"RHa65uclcbZyMN7GUVkdfGtD69MrRThUOsidvtsKxK0=","nbf":1629353792,"tid":"7b00ecdd-385b-46f3-a364-bc40c78b2149","add":"0x0bfd8b6d9c83e4018b6209f528f0e98f7f796ae45d93d0c7e405db8696c64190109b011d0733f2973ed6c9e35ffb4e3c63d610ae3448f70231bbed3b52d829f41c"}
    print(proof)
    print('\n')
    print(claim)

    # create hash of claim_string
    hashed_claim = encode_defunct(text=claim_string) # todo remove hash or use different hasing

    # separate out public key from claim
    public_key = claim['iss'].split(':')[2]

    # try to recover signing public-key. This should be same as public_key above
    signing_public_key = w3.eth.account.recover_message(hashed_claim, signature=proof) 
    print(signing_public_key)
    
    if signing_public_key != public_key:
      raise Exception('Could not verify the identity of the user')


    # Now verify that email and walletAddress sent are authentic too
    additional_proof = claim['add']
    additional_claim = additional_data_string
    hashed_additional_claim = encode_defunct(text=additional_claim)
    print('\n-=================-\n')
    additional_signing_public_key = w3.eth.account.recover_message(hashed_additional_claim, signature=additional_proof)
    print(additional_signing_public_key)

    if additional_signing_public_key != public_key:
      raise Exception('Could not verify email and walletAddress')

    return jsonify({ 'message': 'Successfully verified user' }), 200

  except BaseException as e:
    print(traceback.format_exc())
    return jsonify({ 'message': str(e) }), 400


if __name__ == '__main__':
  app.run(host='0.0.0.0', port=5000)