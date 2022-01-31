int removeDuplicates(int* nums, int numsSize){
    int j=1;
    if(numsSize==0){
        return 0;
    }
    else if(numsSize==1){
        return 1;
    }
    for(int i=1;i<numsSize;i++){
        if(nums[i]!=nums[i-1]){
            nums[j]=nums[i];
            j++;
        }
    }
    return j;
}