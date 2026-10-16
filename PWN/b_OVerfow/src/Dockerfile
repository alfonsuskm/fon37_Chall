FROM gcc:12-bookworm AS build

WORKDIR /build
COPY chall.c .

RUN gcc chall.c -o chall \
    -no-pie \
    -fno-stack-protector \
    -Wl,-z,relro \
    -Wl,-z,noexecstack \
    -Wno-implicit-function-declaration \
    -O0 -g


FROM debian:bookworm-slim

RUN apt-get update && apt-get install -y --no-install-recommends \
    socat \
    && rm -rf /var/lib/apt/lists/*

RUN useradd -m -s /usr/sbin/nologin ctf

WORKDIR /home/ctf
COPY --from=build /build/chall ./chall
COPY flag.txt ./flag.txt

RUN chmod 755 ./chall && \
    chmod 444 ./flag.txt && \
    chown -R root:root /home/ctf && \
    chmod 755 /home/ctf

RUN echo "* hard core 0" >> /etc/security/limits.conf

USER ctf

EXPOSE 1337
CMD ["socat", "-lf", "/dev/stdout", "TCP-LISTEN:1337,reuseaddr,fork", \
     "EXEC:'stdbuf -o0 -e0 ./chall'"]