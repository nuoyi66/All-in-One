#include <stdio.h>
#include <malloc.h>
#define buffersize 5
int processnum=0;
struct pcb
{
    int flag;
    int numlabel;
    char product;
    char state;
    struct pcb*processlink;
}*exe=NULL,*over=NULL;
typedef struct pcb PCB;
PCB *readyhead=NULL,*readytail=NULL;
PCB *consumerhead=NULL,*consumertail=NULL;
PCB *producerhead=NULL,*producertail=NULL;
int productnum=0;
int full=0,empty=buffersize;
char buffer[buffersize];
int bufferpoint=0;
void linklist(PCB* p, PCB* listhead)
{
    PCB *cursor=listhead;
    while(cursor->processlink!=NULL)
    {
        cursor=cursor->processlink;
    }
    cursor->processlink=p;
}
void freelink(PCB*linkhead)
{
    pcb *p;
    while(linkhead!=NULL)
    {
        p=linkhead;
        linkhead=linkhead->processlink;
        free(p);
    }
}
void linkqueue(PCB*process,PCB ** tail)
{
    if (*tail!=NULL)
    {
        (*tail)->processlink=process;
        (*tail)=process;
    }
    else printf("队列未初始化！");
}
PCB *getq(PCB *head,PCB ** tail)
{
    PCB *p;
    p=head->processlink;
    if (p!=NULL)
    {
        head->processlink=p->processlink;
        p->processlink = NULL;
        if(head->processlink==NULL) (*tail)=head;
    }
    else return NULL;
    return p;
}

bool processproc(){
    int i,f,num;
    char ch;
    PCB *p=NULL;
    PCB ** P1=NULL;
    printf("\n请输入希望产生的进程个数：");
    scanf("%d",&num);
    getchar();
    for(i=0;i<num;i++)
    {
        printf("\n请输入希望产生的进程：输入1为生产者进程；输入2为消费者进程\n");
        scanf("%d",&f);
        getchar();
        p=(PCB*)malloc(sizeof(PCB));
        if(!p)
        {
            printf("内存分配失败！");
            return false;
        }
        p->flag=f;
        processnum++;
        p->numlabel=processnum;
        p->state='w';
        p->processlink=NULL;
        if(p->flag==1)
        {
            printf("您要产生的进程是生产者，它是第%d个进程 。请您输入您要该进程产生的字符：\n",processnum);
            scanf("%c",&ch);
            getchar();
            p->product=ch;
            productnum++;
            printf("您要该进程产生的字符是% c\n",p->product);
        }
        else
        {
             printf("您要产生的进程是消费者，它是第%d个进程。\n",p->numlabel);
        }
        linkqueue(p,&readytail);
    }
    return true;
}
bool hasElement(PCB *pro) {
    // 判断队列中是否有进程存在
    if (pro->processlink == NULL)  
    {
        return false;
    } 
    else
     {
        return true;
    }
}
bool waitempty()
{
    if(empty<=0)
    {
        printf("进程%d:缓冲区存数，缓冲区满，该进程进入生产者等待队列\n", exe->numlabel);
        linkqueue(exe,&producertail);
        return false;
    }
    else 
    {
        empty -- ;
        return true;
    }
}

void signalempty()
{
    PCB *p;
    if(hasElement(producerhead)){
        p=getq(producerhead,&producertail);
        linkqueue(p,&readytail);
        printf("等待中的生产者进程进入就绪队列，它的进程号是%d\n",p->numlabel);
    }
    empty ++;
}
bool waitfull()
{
    if(full<=0)
    {
        printf("进程%d:缓冲区存数，缓冲区空，该进程进入消费者等待队列\n", exe->numlabel);
        linkqueue(exe,&consumertail);
        return false;
    }
    else 
    {
        full -- ;
        return true;
    }
}
void signalfull()
{
    PCB *p;
    if(hasElement(consumerhead)){
        p=getq(consumerhead,&consumertail);
        linkqueue(p,&readytail);
        printf("等待中的消费者进程进入就绪队列，它的进程号是%d\n",p->numlabel);
    }
    full++;
}
void producerrun()
{
    if(!waitempty())
    {
        return;
    }
    printf("进程%d开始向缓冲区存数%c\n",exe->numlabel,exe->product);
    buffer[bufferpoint]=exe->product;
    bufferpoint++;
    printf("进程%d向缓冲区存数操作结束\n",exe->numlabel);
    signalfull();
    linklist(exe,over);
}
void comsuerrun()
{
    if(!waitfull())
    {
        return;
    }
    printf("进程%d开始从缓冲区取数\n",exe->numlabel);
    exe ->product=buffer[bufferpoint-1];
    bufferpoint--;
    printf("进程%d从缓冲区取数操作结束，取数结果是%c\n",exe->numlabel,exe->product);
    signalempty();
    linklist(exe,over);
}
void display(PCB* p) //显示进程
{
    p=p->processlink;
    while(p!=NULL)
    {
        printf("进程号：%d,它是一个\n",p->numlabel);
        p->flag==1?printf("生产者\n"):printf("消费者\n");
        p=p->processlink;
    }
}

int main()
{
    char terminate=' ';
    bool element;
    printf("你想开始程序吗?(y/n)");
    scanf("%c",&terminate);
    getchar();
    readyhead=(PCB*)malloc(sizeof(PCB));
    if(readyhead==NULL) return 0;
    readytail = readyhead;
    readyhead->flag=3;
    readyhead->numlabel=processnum;
    readyhead->state='w';
    readyhead->processlink=NULL;
    consumerhead=(PCB*)malloc(sizeof(PCB));
    if(consumerhead==NULL) return 0;
    consumertail = consumerhead;
    consumerhead->processlink=NULL;
    consumerhead->flag=4;
    consumerhead->numlabel=processnum;
    consumerhead->state='w';
    consumerhead->processlink=NULL;
    producerhead=(PCB*)malloc(sizeof(PCB));
    if(producerhead==NULL) return 0;
    producertail=producerhead;
    producerhead->processlink=NULL;
    producerhead->flag=5;
    producerhead->numlabel=processnum;
    producerhead->state='w';
    producerhead->processlink=NULL;
    over=(PCB*)malloc(sizeof(PCB));
    if(over==NULL) return 0;
    over->processlink=NULL;
    while(terminate=='y')
    {
        if(!processproc()) break;
        element=hasElement(readyhead);
        while(element)
        {
            exe=getq(readyhead,&readytail);
            printf("进程%d申请运行，它是一个",exe->numlabel);
            exe->flag==1?printf("生产者\n"):printf("消费者\n");
            if(exe->flag==1)
            {
                producerrun();
            }
            else
            {
                comsuerrun();
            }
            element=hasElement(readyhead);
        }
        printf("就绪队列没有进程\n");
        if(hasElement(consumerhead))
        {
            printf("消费者等待队列中有进程\n");
            display(consumerhead);
        }
        else
        {
            printf("消费者等待队列中没有进程\n");
        }
        if(hasElement(producerhead))
        {
            printf("生产者等待队列有进程\n");
            display(producerhead);
        }
        else
        {
            printf("生产者等待队列中没有进程\n");
        }
        printf("你想继续吗？（press 'y'for on）");
        scanf("%c",&terminate);
        getchar();
    }
    printf("\n\n进程模拟完成.\n");
    freelink(over);
    over=NULL;
    freelink(readyhead);
    readyhead=NULL;
    readytail=NULL;
    freelink(consumerhead);
    consumerhead=NULL;
    consumertail=NULL;
    freelink(producerhead);
    producerhead=NULL;
    producertail=NULL;
    getchar();
    return 0; 
}