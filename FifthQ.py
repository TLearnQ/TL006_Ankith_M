def process_reports(lines):
    total = 0
    written = 0

    try:
        out = open("audit.log", "w")
    except Exception as e:
        print("cannot open audit.log:", e)
        return

    for line in lines:
        total += 1
        try:
            text = line.strip()
            if "ERROR" in text or "WARN" in text or "WARNING" in text:
                out.write(text + "\n")
                written += 1
        except Exception:
            pass

    out.close()
    print("total lines:", total)
    print("error lines:", written)


logs = ["INFO: Connection successful",
        "ERROR: Timeout",
        "INFO: Retry"]

process_reports(logs)