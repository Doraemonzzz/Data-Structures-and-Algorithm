List Merge( List L1, List L2 ){
  List r;
  PtrToNode tmp=(List)malloc(sizeof(struct Node));
  List a=L1->Next;
  List b=L2->Next;
  r=tmp;
  tmp->Next=NULL;
  while(a!=NULL&&b!=NULL){
    if(a->Data<b->Data){
      r->Next=a;
      a=a->Next;
      r=r->Next;
    }
    else{
      r->Next=b;
      b=b->Next;
      r=r->Next;
    }
  }
  r->Next=NULL;
  if (a!=NULL) r->Next=a;
  if (b!=NULL) r->Next=b;
  L1->Next=NULL;
  L2->Next=NULL;
  return tmp;
}
