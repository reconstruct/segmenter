
# TODO: The code below is a simple copy from David's point cloud copy  in S3
# Need to completely rewrite it to use the passed variables

from copy import deepcopy
from datetime import datetime
import os
import json

def transform_dataset(project_id, all_PID=False):
    
    '''
    log_name = setup_logging()

    log.info(f'Source project: {source_project_id}')
    log.info(f'Target project: {target_project_id}')
    log.info(f'Dry Run: {dry_run}')

    source_mongo_uri = os.environ.get('SOURCE_MONGO_URI')
    source_mongo_name = os.environ.get('SOURCE_MONGO_NAME')
    source_db_connection = DBConnection(source_mongo_uri, source_mongo_name, dry_run)
    target_mongo_uri = os.environ.get('TARGET_MONGO_URI')
    target_mongo_name = os.environ.get('TARGET_MONGO_NAME')
    target_db_connection = DBConnection(target_mongo_uri, target_mongo_name, dry_run)

    try:
        migrate_database(source_project_id, target_project_id,
                         source_db_connection, target_db_connection, log_name, dry_run)
    except Exception as e:
        log.exception(e)
    '''