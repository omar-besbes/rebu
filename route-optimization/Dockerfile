# Use Go base image
FROM golang:1.23

# Set working directory
WORKDIR /app

# Copy go.mod and install dependencies
COPY go.mod .
COPY go.sum .
RUN go mod tidy

# Copy the rest of the application
COPY . .

# Compile app
RUN go build

# Command to run the app
CMD ["./route-optimization"]
