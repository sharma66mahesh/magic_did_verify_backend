import unittest
from decoder import decode_did


class TestDecoder(unittest.TestCase):

    def test_decode_did(self):
        request_json = {
            "idToken": "WyIweGZmZmNiYzA1ODQyYmIyMGY0MWE2YTg5YjgyZGVmMDFhZDkxYzFmZjQ2N2RlOTc2NTM0NzE4ZDI0ZTZlOWM1NDE1ZjY5MzM5MTllZjEyNmY3NTBjY2E2ZTk5MDBiOTZiNTA4YzgwNjYxNjgxMjliYzU2NmI2OTAzZmYwMDA3NGRkMWIiLCJ7XCJpYXRcIjoxNjI5MzYzNDU1LFwiZXh0XCI6MTYyOTM2NDM1NSxcImlzc1wiOlwiZGlkOmV0aHI6MHgwNjc5QjIzNjM2RmY1OEUzOUZGODBGZjYzNTVCNDcwZTJDNTdlNkE1XCIsXCJzdWJcIjpcIl9qdnBJSXgzUFNQSUJUdFRDZXlpSDJ4a0xaUHpmbFRZWnFvUkVTbjRTZTg9XCIsXCJhdWRcIjpcIlJIYTY1dWNsY2JaeU1ON0dVVmtkZkd0RDY5TXJSVGhVT3NpZHZ0c0t4SzA9XCIsXCJuYmZcIjoxNjI5MzYzNDU1LFwidGlkXCI6XCI0ZGI4MjY3Yi02MjljLTRiMjUtODNiMi1kYjQ0NmRkNDk2N2RcIixcImFkZFwiOlwiMHg5YzAwZWE4OTgxYTlmYjQ1ODM1NDM1YzJjNzI2NWRmYjg0ODIyMjhjYWJjMGE3NDg3M2IyYzdkNjEwNDQ3ZDZkNDA1MTM3Njc0ZGQxZWJkZGEwOThkNTg2MGI2YmNkMjc1NmI3NzExZTRjYzUzN2MwNWE0ZjM1MWJhNDQwMTBlMzFiXCJ9Il0=",
            "additionalData": "{\"email\":\"prsnakrki@gmail.com\",\"walletAddress\":\"hxfa94343e66fbed10ab26c7bbd9a77fbaee9e710d\"}"}

        decode_did(request_json)
        self.assertTrue(True)
