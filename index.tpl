<html>
  <head>
    <title>{{name}} vous propose...</title>
    <link rel="stylesheet" href="assets/style.css" type="text/css"></link>
    <link href='https://fonts.googleapis.com/css?family=Reenie+Beanie|Lato:300' rel='stylesheet' type='text/css'>
    <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/font-awesome/4.4.0/css/font-awesome.min.css">
  </head>
  <body>
    <div class="wrapper">
      <div class="column1">
        <img src="assets/{{image}}" />
      </div>
      <div class="column2">
        <div class="intro">Pas d’idée de plat à cuisiner ?</div>
        <h1>{{name}} vous propose :</h1>
        <div>
          <ul class="ingredients fa-ul">
            %for ingredient in ingredients:
              <li><i class="fa-li fa fa-heart"></i>{{ingredient}}</li>
            %end
          </ul>
        </div>
        <div class="outro">
          <a href="/">Une autre !</a>
        </div>
      </div>
    </div>
  </body>
</html>



%if True == 'World':
  <!--yolo-->
%else:
  <!--yolo-->
%end
