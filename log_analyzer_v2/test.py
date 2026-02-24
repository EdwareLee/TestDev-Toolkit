from log_analyzer import analyze_log

if __name__ == "__main__":
    logs = [
        "2026-02-10 14:25:01 ERROR [user_login] from 192.168.1.105: auth failed (code: E1001)",
        "2026-02-10 14:26:30 ERROR [payment] from 10.0.0.2: timeout (code: E2005)",
        "2026-02-10 14:27:11 ERROR [user_login] from 192.168.1.105: invalid token (code: E1001)"
    ]

    result = analyze_log(logs)
    print(result)