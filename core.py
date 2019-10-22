result = dict() # {email: [success:failure]}


def statistics_collection(func):
    def wrapper():
        open_session = dict()  # {session id: email}
        with open('jino/maillog', 'r') as log_file:
            for log in log_file:
                if 'sasl_method=LOGIN' in log:
                    open_session[log.split(': ')[1]] = log.split('sasl_username=')[-1][:-1]
                elif 'removed' in log:
                    if log.split(': ')[1] in open_session:
                        del open_session[log.split(': ')[1]]
                elif 'to=' in log:
                    session_id = log.split(': ')[1]
                    if session_id in open_session:
                        sender = open_session[session_id]
                        if sender not in result:
                            result[sender] = [0, 0]
                        if 'status=sent' in log:
                            result[sender][0] += 1
                        elif 'status=bounced' in log or 'status=expired' in log:
                            result[sender][1] += 1
        func()
    return wrapper


@statistics_collection
def output_statistics_collection():
    output = open('output_SC.txt', 'w')
    for key, value in result.items():
        output.write("{0}: {1} {2}\n".format(key, value[0], value[1]))
    output.close()


@statistics_collection
def print_statistics_collection():
    for key, value in result.items():
        print("{0}: {1} {2}\n".format(key, value[0], value[1]))
