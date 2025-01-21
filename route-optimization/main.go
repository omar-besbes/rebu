package main

import (
	"log"
	"os"

	"github.com/gin-gonic/gin"
	"github.com/joho/godotenv"
)

func main() {
	// Load environment variables from .env file
	err := godotenv.Load()
	if err != nil {
		log.Fatalf("Error loading .env file: %v", err)
	}

	// Get values from environment variables
	bestRouteURL := os.Getenv("BEST_ROUTE_URL")
	closestRouteURL := os.Getenv("CLOSEST_ROUTE_URL")
	port := os.Getenv("PORT")

	if port == "" {
		port = "8080" // Default port if not set
	}

	// Initialize Gin router
	router := gin.Default()

	// Define endpoints
	router.POST(bestRouteURL, func(c *gin.Context) {
		log.Printf("Calculating best route ...")

		c.JSON(200, gin.H{
			"type": "best_route",
			"rider": gin.H{
				"name":     "John Doe",
				"location": "Point A",
			},
			"customer_location":    "Point B",
			"customer_destination": "Point C",
			"route":                []string{"Point A", "Point B", "Point C"},
		})
	})

	router.POST(closestRouteURL, func(c *gin.Context) {
		c.JSON(200, gin.H{
			"type": "closest_available_rider",
			"rider": gin.H{
				"name":     "Jane Smith",
				"location": "Point D",
			},
			"customer_location":    "Point E",
			"customer_destination": "Point F",
		})
	})

	// Start the server
	log.Printf("Starting server on port %s...", port)
	router.Run(":" + port)
}
