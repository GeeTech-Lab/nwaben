from nwaben.settings import DEBUG

if DEBUG:
    # test key
    PAYSTACK_SECRET_KEY = 'sk_test_8644da1b3e6afdc8e528ace9c268e231eadf1c56'
    PAYSTACK_PUBLIC_KEY = 'pk_test_deccf766e2b4ccaf1481e28f39003a23b22785a4'
else:
    # live key
    PAYSTACK_SECRET_KEY = 'sk_live_05dbbacb6c4bff68720719669e5e3e550ee88940'
    PAYSTACK_PUBLIC_KEY = 'pk_live_31ccac29d4b49a6b22e99744199ecd4c43ab3b62'