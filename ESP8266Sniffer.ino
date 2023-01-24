#include <Ethernet.h>
#include <SPI.h>

byte mac[] = { 0xDE, 0xAD, 0xBE, 0xEF, 0xFE, 0xED };
IPAddress server(your_server_here);
EthernetClient client;

void setup() {
  Ethernet.begin(mac);
  client.connect(server, 80);
}

void loop() {
  Ethernet.buffer(2048);
  int packetSize = Ethernet.packetReceive();
  int len = Ethernet.packetLoop(packetSize);
  if (len == 0) return;
  client.write(Ethernet.buffer, len);
  client.flush();
}
