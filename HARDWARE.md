# Хардуерно обезпечение / Hardware Requirements

## Български / Bulgarian

### За какво е необходим хардуер?

BitHome Protocol е протокол, базиран на Nostr, който не изисква специален хардуер. Протоколът дефинира само формат на събития и правила за публикуване на обяви за недвижими имоти.

### Минимални изисквания

#### За клиенти (потребители):

- **Устройство**: Всяко съвременно устройство с интернет браузър
  - Компютър (Windows, macOS, Linux)
  - Смартфон (iOS, Android)
  - Таблет
- **Интернет връзка**: Стабилна интернет връзка
- **Браузър**: Актуален уеб браузър (Chrome, Firefox, Safari, Edge)
- **Памет**: Минимум 2 GB RAM
- **Процесор**: Всеки съвременен процесор (от последните 5-7 години)

#### За разработчици:

- **Устройство**: Компютър за разработка
- **Памет**: Минимум 4 GB RAM (препоръчват се 8 GB)
- **Процесор**: Съвременен процесор с поне 2 ядра
- **Дисково пространство**: 
  - Минимум 500 MB за среда за разработка
  - Допълнително пространство за зависимости и инструменти
- **Софтуер**:
  - Git
  - Текстов редактор или IDE (VS Code, WebStorm, Vim и т.н.)
  - Node.js (за JavaScript имплементации)
  - Инструменти за работа с JSON

#### За оператори на Nostr relay:

Ако желаете да стартирате собствен Nostr relay за BitHome събития:

- **Процесор**: 
  - Минимум: 2 CPU ядра
  - Препоръчително: 4+ CPU ядра за голям мащаб
- **Памет**:
  - Минимум: 4 GB RAM
  - Препоръчително: 8-16 GB RAM за голям мащаб
- **Дисково пространство**:
  - Минимум: 20 GB SSD
  - Препоръчително: 100+ GB SSD в зависимост от обема събития
- **Мрежа**:
  - Стабилна интернет връзка
  - Минимум: 10 Mbps симетрична
  - Препоръчително: 100+ Mbps за публични relay
  - Статичен IP адрес (за публични relay)
  - Отворени портове за WebSocket връзки (обикновено 443 или 7000)
- **Операционна система**: Linux (Ubuntu 20.04+, Debian 11+) или Docker

### Специални бележки

1. **Не е необходим специализиран хардуер**: Протоколът работи с всяка Nostr имплементация
2. **Няма mining изисквания**: За разлика от Bitcoin, не е необходим хардуер за mining
3. **Децентрализация**: Можете да използвате съществуващи публични Nostr relay вместо да стартирате собствен
4. **Мащабируемост**: Изискванията зависят от обема на трафика и броя събития

---

## English

### What is hardware needed for?

BitHome Protocol is a Nostr-based protocol that does not require specialized hardware. The protocol only defines event formats and rules for publishing real estate listings.

### Minimum Requirements

#### For Clients (Users):

- **Device**: Any modern device with internet browser
  - Computer (Windows, macOS, Linux)
  - Smartphone (iOS, Android)
  - Tablet
- **Internet Connection**: Stable internet connection
- **Browser**: Modern web browser (Chrome, Firefox, Safari, Edge)
- **Memory**: Minimum 2 GB RAM
- **Processor**: Any modern processor (from the last 5-7 years)

#### For Developers:

- **Device**: Development computer
- **Memory**: Minimum 4 GB RAM (8 GB recommended)
- **Processor**: Modern processor with at least 2 cores
- **Disk Space**: 
  - Minimum 500 MB for development environment
  - Additional space for dependencies and tools
- **Software**:
  - Git
  - Text editor or IDE (VS Code, WebStorm, Vim, etc.)
  - Node.js (for JavaScript implementations)
  - JSON tooling

#### For Nostr Relay Operators:

If you want to run your own Nostr relay for BitHome events:

- **Processor**: 
  - Minimum: 2 CPU cores
  - Recommended: 4+ CPU cores for large scale
- **Memory**:
  - Minimum: 4 GB RAM
  - Recommended: 8-16 GB RAM for large scale
- **Disk Space**:
  - Minimum: 20 GB SSD
  - Recommended: 100+ GB SSD depending on event volume
- **Network**:
  - Stable internet connection
  - Minimum: 10 Mbps symmetric
  - Recommended: 100+ Mbps for public relays
  - Static IP address (for public relays)
  - Open ports for WebSocket connections (typically 443 or 7000)
- **Operating System**: Linux (Ubuntu 20.04+, Debian 11+) or Docker

### Special Notes

1. **No specialized hardware required**: The protocol works with any Nostr implementation
2. **No mining requirements**: Unlike Bitcoin, no mining hardware is needed
3. **Decentralization**: You can use existing public Nostr relays instead of running your own
4. **Scalability**: Requirements depend on traffic volume and number of events

---

## Reference Implementations

### Popular Nostr Relay Software:

- **nostr-rs-relay** - Rust implementation
  - Repo: https://github.com/scsibug/nostr-rs-relay
  - Requirements: Minimal, efficient
  
- **strfry** - High-performance C++ relay
  - Repo: https://github.com/hoytech/strfry
  - Requirements: Low resource usage
  
- **Relay on Node.js** - JavaScript implementation
  - Various implementations available
  - Requirements: Node.js runtime

### Hosting Options:

- **Self-hosted**: VPS or dedicated server
  - DigitalOcean, Linode, Hetzner, AWS, etc.
  - Typical cost: $5-20/month for basic relay
  
- **Docker**: Container deployment
  - Can run on any platform supporting Docker
  - Easier maintenance and updates

---

## FAQ

**Q: Do I need a Bitcoin node to use BitHome Protocol?**  
A: No. While BitHome is Bitcoin-native (uses sats pricing), you don't need to run a Bitcoin node to publish or consume listings.

**Q: Can I use a mobile device as a relay?**  
A: While technically possible, it's not recommended. Mobile devices have limited uptime, bandwidth, and battery. Public relays should run on stable servers.

**Q: What about storage for historical data?**  
A: Storage requirements grow with time. A relay storing all BitHome events might need 1-10 GB per year depending on adoption. Use SSD for better performance.

**Q: Do I need special cryptographic hardware?**  
A: No. Standard CPU cryptographic operations (signing Nostr events with secp256k1) are sufficient and fast on modern processors.
