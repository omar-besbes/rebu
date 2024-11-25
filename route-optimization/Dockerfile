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

# Command to run the app
CMD ["go", "run", "main.go"]
