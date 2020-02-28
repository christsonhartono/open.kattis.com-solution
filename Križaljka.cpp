#include<iostream>
#include<cstring>
using namespace std;

int main(){
	int posH, posV;
	char crossWord[32][32];
	
	cin>>word1>>word2;
	
	for(int i=0; i<strlen(word1); i++){
		int loc=0;
		int found=0;
		for(int j=0; j<strlen(word2); j++){
			if(word1[i]==word2[j]){
				found = 1;
				break;
			}
			loc++;
		}
		if(found==1){
			posH = loc;
			posV = i;
			break;
		}
	}
	
	for(int i=0; i<strlen(word2); i++){
		for(int j=0; j<strlen(word1); j++){
			if(i==posH){
				cout<<word1[j];
			}else if(j==posV){
				cout<<word2[i];
			}else{
				cout<<'.';
			}
		}
		cout<<endl;
	}
	
	return 0;
}
