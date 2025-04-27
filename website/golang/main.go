package main

import (
	"fmt"
	"net/http"

	"github.com/prometheus/client_golang/prometheus"
	"github.com/prometheus/client_golang/prometheus/promhttp"
)

// 🔢 Counter untuk endpoint /
var homeCounter = prometheus.NewCounterVec(
	prometheus.CounterOpts{
		Name: "golang_home_requests_total",
		Help: "Total number of requests to / endpoint",
	},
	[]string{"method", "endpoint"}, // Label untuk filter metrik
)

func main() {
	// 📦 Register custom metric
	prometheus.MustRegister(homeCounter)

	// 🏠 Route /
	http.HandleFunc("/", func(w http.ResponseWriter, r *http.Request) {
		// 🚀 Increment Counter berdasarkan method dan endpoint
		homeCounter.WithLabelValues(r.Method, "/").Inc()
		fmt.Fprintln(w, "Hello from Golang Web App with Prometheus Metrics!")
	})

	// 📊 Route /metrics
	http.Handle("/metrics", promhttp.Handler())

	fmt.Println("Listening on port 8080")
	http.ListenAndServe(":8080", nil)
}
