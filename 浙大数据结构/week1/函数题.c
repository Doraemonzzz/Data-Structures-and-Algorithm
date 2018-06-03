Position BinarySearch( List x, ElementType y ){
  int low=1;
  int high=x->Last;
  int mid;
  while(low<=high){
    mid=(low+high)/2;
    if(x->Data[mid]==y)  
        return mid;  
    else if(x->Data[mid]>y)  
        high=mid-1;  
    else  
        low=mid+1;
  }
  return NotFound;
}
