# NRF
## NRF pinouts



## why can't NRF communicate with wifi though the operate at the same frequency?

**due to protocol,modulation and communication differences**
--> NRF uses Gaussian frequency shift keying modulation 
--> WIFI uses DSS, OFDM,CCK
//these different modulation mean that wifi cannot decode nrf signals and vice versa

**protocols**
-->nRF24L01 operates using a simple packet-based communication protocol (Enhanced ShockBurst), designed for low-power, low-data-rate applications.

-->Wi-Fi follows the IEEE 802.11 standard, which includes complex networking features like authentication, encryption, and error correction.

//Since the two devices do not follow the same protocol rules, they cannot interpret each other's signals

**channels**
-->nRF24L01 typically uses 1 MHz or 2 MHz bandwidth per channel.
-->Wi-Fi uses much wider channels, typically 20 MHz, 40 MHz, or more.
//Wi-Fi signals occupy a much broader spectrum, making it impossible for nRF to interpret Wi-Fi transmissions.

## how to avoid interfence and decrease noises for nrf communication?
 reduce interference and noise, use: ✅ Channels 120–125 to avoid Wi-Fi overlap.
✅ Lower TX power for nearby devices.
✅ Capacitors for power supply filtering.
✅ Short SPI wires & ground plane to reduce EMI.
✅ Shielding & external antennas for better reception.
✅ FHSS (Frequency Hopping) for dynamic interference avoidance.
