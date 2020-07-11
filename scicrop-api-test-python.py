import requests
import logging
import json


def sender_job(url, resume):
    """
    :param post_resume: json_format (dict), resume to send
    :param url: str, url
    """
    try:
        logging.info('sending resume...')
        headers = {'Content-Type': 'application/json'}
        request = requests.post(url, json=resume, headers=headers)
        request.raise_for_status()
        logging.info(request.status_code)
        logging.info('done!')
        return request.status_code
    except Exception as e:
        logging.error('sender_job error: ' + str(e) + '\n')


if __name__ == '__main__':
    logging.basicConfig(level=logging.DEBUG, format='%(asctime)s-%(levelname)s-%(message)s')
    logging.disable(logging.DEBUG)
    with open('./resume_job.json') as f:
        resume = json.load(f)

    result = sender_job('https://engine.scicrop.com/scicrop-engine-web/api/v1/jobs/post_resume', resume)




