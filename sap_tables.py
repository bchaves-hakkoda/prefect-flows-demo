BASE_NAME = "api_response"

# API Endpoint
SAP_TABLES = [
    # location tables
    # {
    #     "url": "https://mmc-s4sap06.mmc.1stbasis.com:44300/sap/opu/odata/sap/Z_T001W_CDS_CDS/Z_T001W_CDS/?$format=json",
    #     "blob_name": f"T001W/{BASE_NAME}.json",
    # },
    # {
    #     "url": "https://mmc-s4sap06.mmc.1stbasis.com:44300/sap/opu/odata/sap/Z_T005T_CDS_CDS/Z_T005T_CDS/?$format=json",
    #     "blob_name": f"T005T/{BASE_NAME}.json",
    # },
    # {
    #     "url": "https://mmc-s4sap06.mmc.1stbasis.com:44300/sap/opu/odata/sap/Z_T005U_CDS_CDS/Z_T005U_CDS/?$format=json",
    #     "blob_name": f"T005U/{BASE_NAME}.json",
    # },
    # {
    #     "url": "https://mmc-s4sap06.mmc.1stbasis.com:44300/sap/opu/odata/sap/Z_TCURC_CDS_CDS/Z_TCURC_CDS/?$format=json",
    #     "blob_name": f"TCURC/{BASE_NAME}.json",
    # },
    # {
    #     "url": "https://mmc-s4sap06.mmc.1stbasis.com:44300/sap/opu/odata/sap/Z_ADRC_CDS_CDS/Z_ADRC_CDS/?$format=json",
    #     "blob_name": f"ADRC/{BASE_NAME}.json",
    # },
    # {
    #     "url": "https://mmc-s4sap06.mmc.1stbasis.com:44300/sap/opu/odata/sap/Z_BUT000_CDS_CDS/Z_BUT000_CDS/?$format=json",
    #     "blob_name": f"BUT000/{BASE_NAME}.json",
    # },
    # {
    #     "url": "https://mmc-s4sap06.mmc.1stbasis.com:44300/sap/opu/odata/sap/Z_BUT052_CDS_CDS/Z_BUT052_CDS/?$format=json",
    #     "blob_name": f"BUT052/{BASE_NAME}.json",
    # },
    # {
    #     "url": "https://mmc-s4sap06.mmc.1stbasis.com:44300/sap/opu/odata/sap/Z_LFA1_CDS_CDS/Z_LFA1_CDS/?$format=json",
    #     "blob_name": f"LFA1/{BASE_NAME}.json",
    # },
    # # Item tables
    # {
    #     "url": "https://mmc-s4sap06.mmc.1stbasis.com:44300/sap/opu/odata/sap/Z_MAKT_CDS_CDS/Z_MAKT_CDS/?$format=json",
    #     "blob_name": f"MAKT/{BASE_NAME}.json",
    # },
    {
        "url": "https://mmc-s4sap06.mmc.1stbasis.com:44300/sap/opu/odata/sap/Z_MARA_CDS_CDS/Z_MARA_CDS/?$format=json",
        "blob_name": f"MARA/{BASE_NAME}.json",
    },
    # {
    #     "url": "https://mmc-s4sap06.mmc.1stbasis.com:44300/sap/opu/odata/sap/Z_MVKE_CDS_CDS/Z_MVKE_CDS/?$format=json",
    #     "blob_name": f"MVKE/{BASE_NAME}.json",
    # },
    # {
    #     "url": "https://mmc-s4sap06.mmc.1stbasis.com:44300/sap/opu/odata/sap/Z_T179_CDS_CDS/Z_T179_CDS/?$format=json",
    #     "blob_name": f"T179/{BASE_NAME}.json",
    # },
    # {
    #     "url": "https://mmc-s4sap06.mmc.1stbasis.com:44300/sap/opu/odata/sap/Z_T179T_CDS_CDS/Z_T179T_CDS/?$format=json",
    #     "blob_name": f"T179T/{BASE_NAME}.json",
    # },
    # # Sales History
    # {
    #     "url": "https://mmc-s4sap06.mmc.1stbasis.com:44300/sap/opu/odata/sap/Z_VBAP_CDS_CDS/Z_VBAP_CDS/?$format=json",
    #     "blob_name": f"VBAP/{BASE_NAME}.json",
    # },
    # {
    #     "url": "https://mmc-s4sap06.mmc.1stbasis.com:44300/sap/opu/odata/sap/Z_VBAK_CDS_CDS/Z_VBAK_CDS/?$format=json",
    #     "blob_name": f"VBAK/{BASE_NAME}.json",
    # },
    # {
    #     "url": "https://mmc-s4sap06.mmc.1stbasis.com:44300/sap/opu/odata/sap/Z_KNA1_CDS_CDS/Z_KNA1_CDS/?$format=json",
    #     "blob_name": f"KNA1/{BASE_NAME}.json",
    # },
    # {
    #     "url": "https://mmc-s4sap06.mmc.1stbasis.com:44300/sap/opu/odata/sap/Z_VBEP_CDS_CDS/Z_VBEP_CDS/?$format=json",
    #     "blob_name": f"VBEP/{BASE_NAME}.json",
    # },
    # {
    #     "url": "https://mmc-s4sap06.mmc.1stbasis.com:44300/sap/opu/odata/sap/Z_VBKD_CDS_CDS/Z_VBKD_CDS/?$format=json",
    #     "blob_name": f"VBKD/{BASE_NAME}.json",
    # },
    # {
    #     "url": "https://mmc-s4sap06.mmc.1stbasis.com:44300/sap/opu/odata/sap/Z_VBFA_CDS_CDS/Z_VBFA_CDS/?$format=json",
    #     "blob_name": f"VBFA/{BASE_NAME}.json",
    # },
    # {
    #     "url": "https://mmc-s4sap06.mmc.1stbasis.com:44300/sap/opu/odata/sap/Z_VBPA_CDS_CDS/Z_VBPA_CDS/?$format=json",
    #     "blob_name": f"VBPA/{BASE_NAME}.json",
    # },
    # Delivery History
    # {
    #     "url": "https://mmc-s4sap06.mmc.1stbasis.com:44300/sap/opu/odata/sap/Z_LIPS_CDS_CDS/Z_LIPS_CDS/?$format=json",
    #     "blob_name": f"LIPS/{BASE_NAME}.json",
    # },
    # {
    #     "url": "https://mmc-s4sap06.mmc.1stbasis.com:44300/sap/opu/odata/sap/Z_LIKP_CDS_CDS/Z_LIKP_CDS/?$format=json",
    #     "blob_name": f"LIKP/{BASE_NAME}.json",
    # },
]
