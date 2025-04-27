FROM golang:1.22

WORKDIR /app

COPY . .

RUN go mod init golang-app && \
    go mod tidy && \
    go build -o main .

EXPOSE 8080

CMD ["./main"]

