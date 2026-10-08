#include<iostream>
using namespace std;

struct node{

int value;
node*next;
};
class linkedlist{
private:
     node*head;
public:
 linkedlist(){
    head=null;
}
void insertfront(int val){
node*newnode=new node;
newnode->value=val;
newnode->next=head;
head=newnode;
}

void deletefirst(){
    if(head==null){
        cout<<"list is empty"<<end l;
        return;
    }
    node*temp=head;
    head=head->next;
    delete temp;
}

void display(){
    node*current=head;
    while(current=!null){
        cout<<current->value<<"";
        current=current->next;
    }
    cout<<end l:
  }
};

int main(){

linkedlist list;
list.insertfront(1);
list.insertfront(2);
list.deletefirst();
list.insertfront(3);
list.deletefirst();
list.insertfront(7);
list.display();


return 0;

}