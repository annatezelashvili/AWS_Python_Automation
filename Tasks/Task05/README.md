### ამოცანა
 დაწერეთ პროგრამები boto3 მოდულის გამოყენებით რომ შექმნათ ლექციაში
გამოყენებული რესურსები. პროექტს მოაყოლეთ მოკლე აღწერა თუ რომელი
პროგრამა რას აკეთებს და როგორ უნდა გამოვიძახოთ. საჭირო რესურსები
მითითებულია ლექციის ბოლოში. დავალება ატვირთეთ გითჰაბზე. დავალება
ფასდება 10 ქულით. დავალების შესრულების საბოლოო თარიღია 23 აპრილი
23:59. 24 აპრილიდან არ განახორციელოთ კომიტები რეპოზიტორიაზე. ლექციაზე
გამოყენებული ლამბდა ფუნქციის კოდი შეგიძლიათ იხილოთ აქ
https://gist.github.com/mikheilibtu/839cde963f68f79e816aacea128039e5


### მოკლე აღწერა

    main.py ფაილში მოცემულია რამდენიმე პროგრამა ,
    1. საცავის შექმნა
    2. ლამბდა ფუნქციის შექმნა ( ეს შეგვეძლო ერთი შეგვექმნა, მაგრამ აქ ყოველ ჯერზე ახალი იქმნება)
    3. ტრიგერის შექმნა ( მას ასევე სჭირდება უფლების მინიჭების ფუნქცია) 
    4. ფაილის ატვირთვა და ლამბდას შესრულებული შედეგის დაბეჭდვა
  
იმისათვის რომ პროგრამამ იმუშაოს, საჭიროა main ფუნქციას გადააწოდოთ შემდეგი პარამეტრები : 
 * **bucket_name**  ახალი საცავის  სახელი
 * **lambda_name**  ახალი ლამბდას სახელი
 * **file_name**  ასატვირთი ფაილის სახელი(ფორმატი უნდა იყოს .jpg)

    შედეგად პროგრამა დაბეჭდავს ატვირთული ფაილზე გამოსახულ ობიექტებს
