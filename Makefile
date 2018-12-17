CC ?= g++

all: music_player

player: music_player.o
	$(CC) -lrt -o $@ $< 

%.o: %.cpp
	$(CC) -c -o $@ $<

clean:
	rm -rf music_player *.o *.bin
