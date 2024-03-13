#include<iostream>
#include<fstream>
#include <ctime>
#include<string>
#include<iomanip>
using namespace std;
string ipv4();
string day();
string hms();
int bandwidth();
int randint(int);
int main(){
	srand(time(NULL));
	ofstream outFile("Bandwidth.csv", ios::app);
        //outFile << "ipv4_addr" << "," << "day" << "," << "hms" << "," << "measured_bandwidth" << endl;
	for(int i=0 ; i<100000 ; i++){
		outFile << ipv4() << "," << day() << "," << hms() << "," << bandwidth() << endl;
	}
}
string ipv4(){
	int num_ip = 6;
        int ip = rand() % 6 + 1;
        switch(ip){
		case 1:
			return "10.22.0.1";
		case 2:
			return "10.22.0.2";
		case 3:
			return "10.22.1.1";
		case 4:
			return "10.22.2.2";
		case 5:
			return "10.22.20.69";
		case 6:
			return "10.22.21.53";
	}
	return 0;	
}
string day(){
	int month = rand() % 12 + 1;
	int day = rand() % 28 + 1;
        // 2021-01-01
	ostringstream oss;
	oss << "2024-" << setfill('0') << setw(2) << month << "-" << setfill('0') << setw(2) << day;
	return oss.str();
}
string hms(){
	int hour = rand() % 24;
        int minute = rand() % 60;
        int sec = rand() % 60;	
        // 00:01:59
	ostringstream oss;
	oss << setfill('0') << setw(2) << hour << ":" << setfill('0') << setw(2) << minute << ":" << setfill('0') << setw(2) << sec;
	return oss.str();
}
int bandwidth(){
	return rand() % 8000 + 1000;
}
