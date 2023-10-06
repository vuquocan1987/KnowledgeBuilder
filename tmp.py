import os

def create_openapi_spec():
    spec = """
openapi: 3.0.0
info:
  title: Addition API
  version: 1.0.0

paths:
  /add:
    post:
      summary: Add two numbers
      requestBody:
        content:
          application/json:
            schema:
              type: object
              properties:
                num1:
                  type: integer
                num2:
                  type: integer
      responses:
        '200':
          description: Successful addition
          content:
            application/json:
              schema:
                type: object
                properties:
                  result:
                    type: integer
"""
    with open('addition_openapi.yaml', 'w') as f:
        f.write(spec)

def create_deployment_spec():
    spec = """
apiVersion: apps/v1
kind: Deployment
metadata:
  name: addition-deployment
spec:
  replicas: 2
  selector:
    matchLabels:
      app: addition-service
  template:
    metadata:
      labels:
        app: addition-service
    spec:
      containers:
      - name: addition-service
        image: your_image_repository/addition-service:latest
        ports:
        - containerPort: 8081
"""
    with open('addition_deployment.yaml', 'w') as f:
        f.write(spec)

def create_prometheus_spec():
    spec = """
apiVersion: monitoring.coreos.com/v1
kind: ServiceMonitor
metadata:
  name: addition-monitor
  labels:
    release: prometheus
spec:
  selector:
    matchLabels:
      app: addition-service
  endpoints:
  - port: addition-port
"""
    with open('addition_prometheus.yaml', 'w') as f:
        f.write(spec)

def create_service_spec():
    spec = """
apiVersion: v1
kind: Service
metadata:
  name: addition-service
spec:
  selector:
    app: addition-service
  ports:
    - name: addition-port
      protocol: TCP
      port: 81
      targetPort: 8081
  type: LoadBalancer
"""
    with open('addition_service.yaml', 'w') as f:
        f.write(spec)

def main():
    create_openapi_spec()
    create_deployment_spec()
    create_prometheus_spec()
    create_service_spec()

if __name__ == '__main__':
    main()



