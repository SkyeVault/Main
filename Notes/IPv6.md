# IPv6 Primer

## What is IPv6?

IPv6 (Internet Protocol version 6) is the successor to IPv4, designed to overcome limitations in address space and simplify network configuration and routing. It uses **128-bit addressing**, allowing for significantly more IP addresses than IPv4.

### IPv4 vs IPv6 Address Capacity

| Protocol | Address Length | Total Addresses |
|----------|----------------|-----------------|
| IPv4     | 32-bit         | 4,294,967,296   |
| IPv6     | 128-bit        | 18,446,744,073,709,551,616 (per /64) |

- A single **/64** IPv6 block contains more addresses than the entire IPv4 space.
- ISPs often receive **/32 allocations**, which can subdivide into:
  - 65,536 `/48` blocks  
  - Each `/48` contains 65,536 `/64` blocks

## IPv6 Address Notation

IPv6 addresses use **colon-separated hexadecimal** instead of dotted decimal (IPv4):

```text
IPv4: 192.168.0.1
IPv6: 2001:0DB8:0000:0003:0000:01FF:0000:002E
```

### Abbreviation Rules

- Leading zeroes can be omitted.
- Contiguous sections of `0000` can be replaced with `::` (once only).

**Valid examples:**
- `2001:DB8::3:0:1FF:0:2E`
- `2001:DB8:0:3:0:1FF::2E`

**Invalid example:**
- `2001:DB8::3::1FF::2E` (multiple `::` not allowed)

## IPv6 Address Types and Structure

### Address Categories

| Address Type | Description | Example |
|--------------|-------------|---------|
| **Unicast** | One-to-one communication | `2001:db8::1` |
| **Multicast** | One-to-many communication | `ff02::1` (all nodes) |
| **Anycast** | One-to-nearest communication | Same as unicast format |

### Special Address Ranges

| Range | Purpose | Notes |
|-------|---------|-------|
| `::1/128` | Loopback | IPv6 equivalent of `127.0.0.1` |
| `::/128` | Unspecified | IPv6 equivalent of `0.0.0.0` |
| `fe80::/10` | Link-local | Auto-configured, not routable |
| `fc00::/7` | Unique Local | Private addresses (like RFC 1918) |
| `2000::/3` | Global Unicast | Public routable addresses |

### Address Structure (Global Unicast)

```text
|  48 bits   |  16 bits  |       64 bits        |
+------------+-----------+----------------------+
| Global     | Subnet    | Interface Identifier |
| Prefix     | ID        | (EUI-64 or Privacy)  |
+------------+-----------+----------------------+
```

## IPv6 Features and Improvements

### Simplified Header Structure
- Fixed 40-byte header (vs variable IPv4)
- No header checksum (offloaded to link layer)
- Extension headers for optional features
- Better router performance

### Built-in Security
- IPSec support mandatory in original spec
- Better support for encryption and authentication
- Reduced NAT dependency improves end-to-end security

### Auto-configuration
- **SLAAC** (Stateless Address Autoconfiguration)
- **DHCPv6** for managed configuration
- Router advertisements for network parameters
- No need for manual IP assignment in many cases

### Quality of Service
- Flow labeling for traffic prioritization
- Better support for real-time applications
- Simplified packet classification

## Transition and Coexistence

### Dual-Stack Operation
- Most systems now support **dual-stack** networking (IPv4 and IPv6 coexisting)
- Applications prefer IPv6 when available (Happy Eyeballs algorithm)
- Fallback to IPv4 for compatibility

### Tunneling Mechanisms
- **6to4**: Automatic tunneling using IPv4 infrastructure
- **Teredo**: NAT traversal for IPv6
- **6rd**: ISP-managed tunneling
- **Hurricane Electric Tunnel Broker**: Popular free service

### Translation Methods
- **NAT64/DNS64**: IPv6-only to IPv4 translation
- **464XLAT**: Mobile carrier translation
- **MAP-T/MAP-E**: Carrier-grade NAT with IPv6

## Operating System Support

| OS / Platform | IPv6 Status                |
|---------------|----------------------------|
| Linux/BSD/macOS | Fully supported, enabled by default |
| Windows Vista / Server 2008+ | Native support enabled |
| Windows XP / 2003 | Optional, limited features |
| iOS/Android | Full support since early versions |
| Network Equipment | Universal support in modern hardware |

Most modern applications (browsers, mail clients, etc.) will use IPv6 automatically if it's available — no special setup required.

## IPv6 in Network Services

### DNS Configuration
- **AAAA records** for IPv6 addresses (vs A records for IPv4)
- **PTR records** in `ip6.arpa` for reverse DNS
- Dual-stack DNS servers recommended

### Web Services
- HTTP/HTTPS work identically over IPv6
- URL format: `http://[2001:db8::1]:8080/path`
- Load balancers and CDNs support IPv6

### Mail Services
- **MX records** work with IPv6 addresses
- SMTP, IMAP, POP3 protocols unchanged
- Anti-spam systems IPv6-aware

## Network Configuration Examples

### Static Configuration (Linux)
```bash
# Add IPv6 address
ip -6 addr add 2001:db8::1/64 dev eth0

# Add default route
ip -6 route add default via 2001:db8::1

# Enable forwarding
echo 1 > /proc/sys/net/ipv6/conf/all/forwarding
```

### Router Advertisement (radvd.conf)
```text
interface eth0 {
    AdvSendAdvert on;
    prefix 2001:db8::/64 {
        AdvOnLink on;
        AdvAutonomous on;
    };
};
```

## Why IPv6 Matters for Developers & Sysadmins

### Technical Benefits
- Enables end-to-end connectivity without NAT
- Required for addressing scale in IoT, large-scale cloud, and decentralization networks
- Improves routing efficiency and multicast handling
- Foundation for modern tunneling, agent communication, and overlay networks

### Business Impact
- **Future-proofing**: IPv4 exhaustion is real
- **Performance**: Reduced NAT overhead
- **Compliance**: Required for many government and enterprise networks
- **Global reach**: Essential for emerging markets

### Development Considerations
- Test applications with IPv6-only networks
- Handle IPv6 address parsing correctly
- Consider address privacy implications
- Plan for dual-stack monitoring and logging

## Security Considerations

### IPv6-Specific Threats
- **Address scanning**: Harder but not impossible
- **Neighbor Discovery attacks**: ICMPv6 flooding
- **Router Advertisement spoofing**: Rogue routers
- **Extension header attacks**: Fragmentation issues

### Best Practices
- Implement proper IPv6 firewall rules
- Monitor ICMPv6 traffic patterns
- Use privacy extensions for client addresses
- Regular security audits of IPv6 configuration
- Disable IPv6 if not used (defense in depth)

## Getting Started with HE.net IPv6 Certification

1. **Newbie**: Basic tunnel setup and connectivity
2. **Explorer**: Web browsing over IPv6
3. **Enthusiast**: Email and DNS configuration
4. **Administrator**: Advanced routing and services
5. **Professional**: Complex network scenarios
6. **Guru**: Expert-level IPv6 deployment

### Certification Benefits
- Hands-on learning with real IPv6 infrastructure
- Free /48 subnet allocation
- Industry-recognized credential
- Access to advanced tunnel features


### Connectivity Problems
```bash
# Test basic connectivity
ping6 google.com

# Check routing table
ip -6 route show

# Verify interface configuration
ip -6 addr show

# Test DNS resolution
nslookup -type=AAAA google.com
```

### Configuration Validation
```bash
# Check if IPv6 is enabled
cat /proc/sys/net/ipv6/conf/all/disable_ipv6

# Monitor neighbor discovery
ip -6 neigh show

# Test tunnel connectivity (HE.net)
ping6 2001:470:0:76::2
```
