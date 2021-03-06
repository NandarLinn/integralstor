#!/usr/bin/python
import sys
from integralstor import remote_replication, tasks_utils, audit


def pause_rsync_remote_replication(remote_replication_id):
    try:
        audit_str = ''
        rr, err = remote_replication.get_remote_replications(
            remote_replication_id)
        if err:
            raise Exception('Could not fetch replication details: %s' % err)

        replication = rr[0]
        mode = replication['mode']
        if mode != 'rsync':
            raise Exception('Invalid replication mode')

        # since the intention is to prevent any further retries as well, check
        # for 'error-retrying' status also.
        running_tasks, err = tasks_utils.get_tasks_by_cron_task_id(replication['cron_task_id'], get_last_by=False, status_list=['running', 'error-retrying'])
        if err:
            raise Exception
        if running_tasks:
            # To prevent re-attempts, mark it 'failed'
            ret, err = tasks_utils.stop_task(running_tasks[0]['task_id'], mark_failed=True)
            if err:
                raise Exception
            audit_str = "%s has been paused, it will resume at the next run schedule" % running_tasks[0]['description']

            audit.audit("stop_background_task",
                        audit_str, None, system_initiated=True )
    except Exception as e:
        return False, 'Error pausing rsync remote replication task: %s' % e
    else:
        return True, None


if __name__ == '__main__':
    # print sys.argv
    if len(sys.argv) != 2:
        print('Usage : python pause_rsync_remote_replication.py remote_replication_id')
        sys.exit(-1)
    ret, err = pause_rsync_remote_replication(sys.argv[1])
    print((ret, err))
    if err:
        sys.exit(-1)
    sys.exit(0)

# vim: tabstop=8 softtabstop=0 expandtab ai shiftwidth=4 smarttab
