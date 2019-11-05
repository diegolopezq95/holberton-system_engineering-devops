#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>

/**
 * infinite_while - sleep 1.
 *
 * Return: Always 0.
 */
int infinite_while(void)
{
	while (1)
	{
		sleep(1);
	}
	return (0);
}

/**
 * main - entry point
 *
 * Return: always 0 (success)
 */
int main(void)
{
	pid_t child_pid;
	unsigned int i;

	for (i = 0; i < 5; i++)
	{
		child_pid = fork();
		if (child_pid == -1)
		{
			perror("Fork failed");
			exit(1);
		}
		else if (child_pid == 0)
		{
			exit(0);
		}
		printf("Zombie process created, PID: %i\n", child_pid);
	}
	infinite_while();
	return (0);
}
