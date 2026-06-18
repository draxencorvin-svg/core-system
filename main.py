from log_parser import parse_logs

if __name__ == "__main__":
    logs = parse_logs("logs/input.log")
    print(len(logs))
