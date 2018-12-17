#include "stdlib.h"

void can_fly_player()
{
	system("play I_believe_I_can_fly.mp3");		// I believe I can fly
}

void cant_fly_player()
{
	system("play falling_from_cloud.mp3");		// Wide Awake
}

int main(int argc, char* argv[])
{
	if(argc == 2)
	{
		if(argv[1]=="y")
		{
			can_fly_player();
		}
		else
		{
			cant_fly_player();
		}
	}
	return 0;
}
