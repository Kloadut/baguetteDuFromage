<html>
  <head>
    <title>{{name}} vous propose...</title>
    <link rel="stylesheet" href="/assets/fonts.css" type="text/css">
    <link rel="stylesheet" href="/assets/style.css" type="text/css">
    <link rel="stylesheet" href="/assets/font-awesome/css/font-awesome.min.css">
    <link rel="icon" href="/assets/favicon.ico?v=1.1"> 
  </head>
  <body>
    <div class="wrapper">
      <div class="column1">
        <img src="/assets/{{image}}" />
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
      </div>
      <div class="footer">
        <div class="buttons">
            %if answer=='yes':
              <a class="miam disabled" href="javascript: void(0)" disabled><i class="fa fa-smile-o"></i> Miam !</a>
            %elif answer=='almost':
              <a class="bof disabled" href="javascript: void(0)" disabled><i class="fa fa-meh-o"></i> Bof</a>
            %elif answer=='no':
              <a class="beurk disabled" href="javascript: void(0)" disabled><i class="fa fa-frown-o"></i> Beurk !</a>
            %else:
              <div class="button-container">
                <a class="miam" href="?answer=yes"><i class="fa fa-smile-o"></i> Miam !</a>
              </div>
              <div class="button-container">
                <a class="bof" href="?answer=almost"><i class="fa fa-meh-o"></i> Bof</a>
              </div>
              <div class="button-container">
                <a class="beurk" href="?answer=no"><i class="fa fa-frown-o"></i> Beurk !</a>
              </div>
            %end 
        </div>
        <div class="outro">
          <a href="/"><i class="fa fa-refresh"></i> Une autre ?</a>
        </div>
      </div>
    </div>
    <!-- score: {{score}} -->
  </body>
</html>
