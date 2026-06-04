IoT stack for LabControl (MQTT + Node-RED + mock publisher)

Services:
- mosquitto: MQTT broker
- nodered: Node-RED UI (http://localhost:1880)
- mock-publisher: small Python publisher that pushes mocked machine metrics to topic `labcontrol/machines/metrics`

How to run:

cd labcontrol-iot
docker compose up --build

Visit Node-RED at http://localhost:1880 and add a MQTT-in node pointed to broker `mosquitto:1883` and topic `labcontrol/machines/metrics` to visualize messages.

Integration with backend later:
- Node-RED can forward messages to the backend via HTTP POST to /api endpoints or use the backend MQTT client to subscribe directly.
