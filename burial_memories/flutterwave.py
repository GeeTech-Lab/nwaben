from nwaben.settings import DEBUG

if DEBUG:
    # test key
    FLUTTERWAVE_SECRET_KEY = 'FLWSECK_TEST-d917ff9b7854fe25486b22ff69ed614d-X'
    FLUTTERWAVE_PUBLIC_KEY = 'FLWPUBK_TEST-e12585f4c2da40025222b13315c5483c-X'
    FLUTTERWAVE_ENCRYPTION_KEY = 'FLWSECK_TEST9f81344e0682'
else:
    # live key
    FLUTTERWAVE_SECRET_KEY = 'FLWSECK-626e1346d882d2ffe7327743e8b5d300-X'
    FLUTTERWAVE_PUBLIC_KEY = 'FLWPUBK-27c6a4a21efd0cf3c5b4fddcdbeecc74-X'
    FLUTTERWAVE_ENCRYPTION_KEY = '626e1346d882050ce798f1a5'