CREATE TABLE IF NOT EXISTS security_logs (
    id SERIAL PRIMARY KEY,
    timestamp TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    source_ip VARCHAR(15),
    destination_ip VARCHAR(15),
    protocol VARCHAR(10),
    port INTEGER,
    event_type VARCHAR(50),
    severity VARCHAR(10),
    description TEXT
);

-- Security logs
INSERT INTO security_logs (source_ip, destination_ip, protocol, port, event_type, severity, description) VALUES
    ('192.168.1.100', '10.0.0.1', 'TCP', 22, 'SSH Brute Force', 'HIGH', 'Multiple failed SSH login attempts'),
    ('10.0.0.15', '192.168.1.200', 'UDP', 53, 'DNS Query', 'LOW', 'Normal DNS resolution'),
    ('172.16.0.5', '10.0.0.2', 'TCP', 80, 'Web Attack', 'MEDIUM', 'SQL Injection attempt detected'),
    ('192.168.1.50', '10.0.0.3', 'TCP', 443, 'SSL Handshake', 'LOW', 'Successful HTTPS connection'),
    ('10.0.0.20', '192.168.1.100', 'ICMP', NULL, 'Ping Scan', 'MEDIUM', 'Network scanning activity detected');
