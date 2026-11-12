
import socket

print("=" * 45)
print("          PORT STATUS CHECKER")
print("=" * 45)

# Get target system details
host = input("Enter IP address or hostname: ").strip()

try:
    port = int(input("Enter port number (1-65535): "))

    if not 1 <= port <= 65535:
        print("Invalid port number! Enter between 1 and 65535.")

    else:
        # Common port services
        services = {
            21: "FTP",
            22: "SSH",
            25: "SMTP",
            53: "DNS",
            80: "HTTP",
            110: "POP3",
            143: "IMAP",
            443: "HTTPS",
            3306: "MySQL",
            8080: "HTTP Alternative"
        }

        service = services.get(port, "Unknown Service")

        print("\nChecking port...")
        print("Host:", host)
        print("Port:", port)
        print("Service:", service)

        # Create TCP connection
        try:
            connection = socket.create_connection(
                (host, port), timeout=3
            )
            connection.close()

            print("\nSTATUS: PORT IS OPEN")
            print("The target is accepting TCP connections.")

        except ConnectionRefusedError:
            print("\nSTATUS: PORT IS CLOSED")
            print("The target refused the connection.")

        except socket.timeout:
            print("\nSTATUS: CONNECTION TIMED OUT")
            print("The target did not respond in time.")

        except socket.gaierror:
            print("\nERROR: Invalid hostname or IP address.")

        except OSError as error:
            print("\nSTATUS: CONNECTION FAILED")
            print("Reason:", error)

except ValueError:
    print("Invalid input! Please enter a numeric port number.")

print("\n" + "=" * 45)
print("          CHECK COMPLETED")
print("=" * 45)
