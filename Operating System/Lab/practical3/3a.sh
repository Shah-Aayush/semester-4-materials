#sdiff three1  three2
#vmdiff three1 three2
#diff three1 three2
#cmp theer1 three2
#comm three1 three2 [works with sorting]
#comm  -12 three1 three2		[only shows similar columns]
echo -e "\nComparing two files using 'sdiff'"
sdiff sample1.txt sample2.txt
echo -e "\nComparing two files using 'vimdiff'"
vimdiff sample1.txt sample2.txt
echo -e "\nComparing two files using 'diff'"
diff sample1.txt sample2.txt
echo -e "\nComparing two files using 'cmp'"
cmp sample1.txt sample2.txt
echo -e "\nComparing two files using 'comm'"
comm sample1.txt sample2.txt
