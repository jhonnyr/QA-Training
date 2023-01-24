environment = {'dev': 'https://dev-icyte-analytics.integrichain.net/',
               'test': 'https://test.integrichain.net/DNAPORTAL/',
               'uat': 'https://uat.integrichain.com/DNAPORTAL/ ',
               'prod': 'https://cloud.integrichain.com/DNAPORTAL/'}

db_name = {"test": "PD_Test",
           "uat": "PD_UAT",
           "prod": ""}

# q_data_source = """SELECT distinct
#                         ds.id data_source_id,
#                         ds.data_source_name
#                     FROM dna_metadata.dna_investigator_data_sources as ds
#                     INNER JOIN dna_admin.dna_capability as cap ON cap.data_source_related = ds.id
#                     INNER JOIN dna_admin.dna_user_role_capability_link capl ON cap.id = capl.dna_capability_id
#                     WHERE
#                         dna_investigator_module_id = 10 AND
#                         capl.dna_user_role_id in (select id from dna_admin.dna_user_role where dna_organization_id = {}) AND
#                         capl.ui_visibility_flag = 'VISIBLE'"""

q_data_source = """SELECT
                        ds.id data_source_id,
                        ds.data_source_name
                    FROM dna_metadata.dna_investigator_data_sources as ds
                    INNER JOIN dna_admin.dna_user_organization_data_sources_link as dsl ON
                        ds.id = dsl.dna_investigator_data_sources_id
                    WHERE
                        dna_investigator_module_id = 10 AND
                        dsl.dna_user_organization_id = {};"""


def map_environment(env):
    return environment[env]


def get_db_name(env):
    return db_name[env]
