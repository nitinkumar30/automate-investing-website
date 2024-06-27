import json

def extract_certificate_attributes(certificate_data):
    try:
        certificate_json = json.loads(certificate_data)
        if "credentialSubject" in certificate_json:
            subject_data = certificate_json["credentialSubject"]
            attributes = {
                "Name": subject_data.get("name", ""),
                "Gender": subject_data.get("gender", ""),
                "Age": subject_data.get("age", ""),
                "Nationality": subject_data.get("nationality", ""),
                "Address": subject_data.get("address", {}).get("streetAddress", ""),
                "City": subject_data.get("address", {}).get("city", ""),
                "Postal Code": subject_data.get("address", {}).get("postalCode", ""),
            }
            return attributes
    except json.JSONDecodeError:
        print("Invalid certificate JSON format")
    return None

file_content = '''
{"osUpdatedAt": "2021-07-11T14:05:28.930Z", "osCreatedAt": "2021-07-11T14:05:28.930Z", "meta": {"date": "2021-06-21T05:30:28.187Z", "osUpdatedAt": "2021-07-11T14:05:28.930Z", "osCreatedAt": "2021-07-11T14:05:28.930Z", "totalDoses": 2, "batch": "batch-02", "name": "Pfizer", "osid": "208b62cf-160c-4b53-b67d-ea069e0aa616", "cit": "00000011", "manufacturer": "ph"}, "contact": ["tel:8788622512"], "certificateId": "623755957", "name": "Bondoc Anderson, Wick ", "mobile": "8788622512", "certificate": "{\"@context\":[\"https://www.w3.org/2018/credentials/v1\",\"https://cowin.gov.in/credentials/vaccination/v1\"],\"type\":[\"VerifiableCredential\",\"ProofOfVaccinationCredential\"],\"credentialSubject\":{\"type\":\"Person\",\"id\":\"19882120590\",\"refId\":\"77889955\",\"name\":\"Bondoc Anderson, Wick \",\"gender\":\"Male\",\"age\":\"33\",\"nationality\":\"PH\",\"address\":{\"streetAddress\":\"Ajoya Subdivision\",\"streetAddress2\":\"\",\"district\":\"Cebu\",\"city\":\"\",\"addressRegion\":\"Homa\",\"addressCountry\":\"IN\",\"postalCode\":\"6015\"}},\"issuer\":\"https://cowin.gov.in/\",\"issuanceDate\":\"2021-07-11T14:05:28.902Z\",\"evidence\":[{\"id\":\"https://cowin.gov.in/vaccine/623755957\",\"feedbackUrl\":\"https://cowin.gov.in/?623755957\",\"infoUrl\":\"https://cowin.gov.in/?623755957\",\"certificateId\":\"623755957\",\"type\":[\"Vaccination\"],\"batch\":\"batch-01\",\"vaccine\":\"Pfizer\",\"manufacturer\":\"ph\",\"date\":\"2021-04-21T05:30:28.187Z\",\"effectiveStart\":\"2021-04-21\",\"effectiveUntil\":\"2022-04-21\",\"dose\":1,\"totalDoses\":2,\"verifier\":{\"name\":\"ss\"},\"facility\":{\"name\":\"Lapu-Lapu Hoops Dome\",\"address\":{\"streetAddress\":\"df\",\"streetAddress2\":\"\",\"district\":\"Cebu\",\"city\":\"\",\"addressRegion\":\"Lapus\",\"addressCountry\":\"IN\",\"postalCode\":\"6015\"}}}],\"nonTransferable\":\"true\",\"proof\":{\"type\":\"RsaSignature2018\",\"created\":\"2021-07-11T14:05:28Z\",\"verificationMethod\":\"did:india\",\"proofPurpose\":\"assertionMethod\",\"jws\":\"eyJhbGciOiJQUzI1NiIsImI2NCI6ZmFsc2UsImNyaXQiOlsiYjY0Il19..GfrISzKN1U8QkxNXXwakqtIckFaqGItD2Cd6-0h8zdUo02RHQxIxrf5AuEKGqKN7WIT2G0i9i4kHIv1FaN7cV6RFv_Hv2gzo86L6t3t6J8jzlfImWg0eAZLa8iTayGd081gs1flp-tH6aUSh6lnCAxZhhiFiFY22UFUwClK27AVlHasHLjjx0zlRWIyl5_zRmhzfrdt7E0Y3p5QQknIXWh-LcBNepYHSJe4NUAxzTtiGWrh22kPDGSh9T1kAjTMOjr_ckOPy2-mvCa3pfOp2M_MHGK2-W-Fm-m-jy5TgIvArQIebVWhkHD_56V6Q2YVm87KUe4GhrayyLoiof9NXkA\"}}", "osid": "def6b2f9-98a6-400c-aa42-728b77ff4b38", "preEnrollmentCode": "77889955", "programId": "VCC001"}
'''

try:
    data = json.loads(file_content)
except json.JSONDecodeError:
    print("Invalid JSON format")
else:
    certificate_data = data.get("certificate")
    if certificate_data:
        attributes = extract_certificate_attributes(certificate_data)
        if attributes:
            print("Certificate Attributes:")
            for key, value in attributes.items():
                print(f"{key}: {value}")


