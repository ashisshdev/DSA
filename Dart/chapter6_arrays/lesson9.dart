// ignore_for_file: unnecessary_null_comparison

class Solution {
  void merge(List<int> nums1, int m, List<int> nums2, int n) {
    List<int> mergedList = [];

    int i = 0;
    int j = 0;
    int? list1Element = nums1[0];
    int? list2Element = nums2[0];

    if (m == 0) {
      mergedList = nums2;
    }
    if (n == 0) {
      mergedList = nums1;
    }
    // heheheheh -------------------------------------
    if (n != 0 && m != 0) {
      print("none of the lists are empty.");
      while (list1Element != null || list2Element != null) {
        print("while Loop started");
        print("merged array now is = ");
        print(mergedList);
        if (list1Element == null) {
          if(list1Element < list2Element!){
                      print("list 1 element is = null, therefore adding list 2 item");
          mergedList.add(list2Element);
          print("list 2 element is added, increasing the count here");
          if (j < n - 1) {
            j++;
            list2Element = nums2[j];
            print("list 2 item now is = " + list2Element.toString());
          } else {
            list2Element = null;
            print("list 2 item set to null");
          }
          continue;
          }
        }

        if (list2Element == null || list1Element > list2Element) {
          print("list 1 item is smaller than list 2 item");
              mergedList.add(list1Element);
              print("list 1 element is added, increasing the count");
              if (i < m-1) {
                i++;
                list1Element = nums1[i];
                print("list 1 item now is = " + list1Element.toString());
              } else {
                list1Element = null;
                print("list 1 item set to null");
              }
              continue;
        }
        //  else {
        //   print("list 1 element is not null");
        //   if (list2Element == null) {
        //     print("list 2 element is = null, therefore adding list 1 element to list");

        //     mergedList.add(list1Element);
        //     print("list 1 element is added, increasing the count here");
        //     if (i < m-1) {
        //       i++;
        //       list1Element = nums1[i];
        //       print("list 1 item now is = " + list1Element.toString());

        //     } else {
        //       list1Element = null;
        //       print("list 1 item set to null");
        //     }
        //     continue;
        //   } else {
        //     if (list1Element < list2Element) {
        //       print("list 1 item is smaller than list 2 item");
        //       mergedList.add(list1Element);
        //       print("list 1 element is added, increasing the count");
        //       if (i < m-1) {
        //         i++;
        //         list1Element = nums1[i];
        //         print("list 1 item now is = " + list1Element.toString());
        //       } else {
        //         list1Element = null;
        //         print("list 1 item set to null");
        //       }
        //       continue;
        //     } else {
        //       print("list 2 item is smaller than list 1 item");

        //       mergedList.add(list2Element);
        //       print("list 2 element is added, increasing the count");
        //       if (j < n-1) {
        //         j++;
        //         list2Element = nums2[j];
        //         print("list 2 item now is = " + list2Element.toString());

        //       } else {
        //         list2Element = null;
        //         print("list 2 item set to null");
        //       }
        //       continue;
        //     }
        //   }
        // }
      }
      print("loop ended haha");
    }
    // heheheheh -------------------------------------

    print(mergedList);
  }
}

void main() {
  List<int> list1 = [1, 2, 3];
  List<int> list2 = [2, 4, 5];
  Solution().merge(list1, 3, list2, 3);

  List<int> list3 = [1, 2, 2, 2, 3, 3, 4, 8];
  List<int> list4 = [2, 4, 4, 5, 7, 9];
  Solution().merge(list3, 8, list4, 6);
}





// if (n != 0 && m != 0) {
//       print("none of the lists are empty.");
//       while (list1Element != null || list2Element != null) {
//         print("while Loop started");
//         print("merged array now is = ");
//         print(mergedList);
//         if (list1Element == null) {
//           print("list 1 element is = null, therefore adding list 2 item");
//           mergedList.add(list2Element!);
//           print("list 2 element is added, increasing the count here");
//           if (j < n-1) {
//             j++;
//             list2Element = nums2[j];
//             print("list 2 item now is = " + list2Element.toString());
            
//           } else {
//             list2Element = null;
//             print("list 2 item set to null");
//           }
//           continue;
//         } else {
//           print("list 1 element is not null");
//           if (list2Element == null) {
//             print("list 2 element is = null, therefore adding list 1 element to list");

//             mergedList.add(list1Element);
//             print("list 1 element is added, increasing the count here");
//             if (i < m-1) {
//               i++;
//               list1Element = nums1[i];
//               print("list 1 item now is = " + list1Element.toString());
              
//             } else {
//               list1Element = null;
//               print("list 1 item set to null");
//             }
//             continue;
//           } else {
//             if (list1Element < list2Element) {
//               print("list 1 item is smaller than list 2 item");
//               mergedList.add(list1Element);
//               print("list 1 element is added, increasing the count");
//               if (i < m-1) {
//                 i++;
//                 list1Element = nums1[i];
//                 print("list 1 item now is = " + list1Element.toString());
//               } else {
//                 list1Element = null;
//                 print("list 1 item set to null");
//               }
//               continue;
//             } else {
//               print("list 2 item is smaller than list 1 item");

//               mergedList.add(list2Element);
//               print("list 2 element is added, increasing the count");
//               if (j < n-1) {
//                 j++;
//                 list2Element = nums2[j];
//                 print("list 2 item now is = " + list2Element.toString());
                
//               } else {
//                 list2Element = null;
//                 print("list 2 item set to null");
//               }
//               continue;
//             }
//           }
//         }
//       }
//       print("loop ended haha");
//     }