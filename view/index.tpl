<html>
Bonjour

%if True == 'World':
    <h1>Ingredients : {{','.split(ingredients)}}!</h1>
    <p>This is a test.</p>
%else:
    <h1>Ingredients : {{','.split(ingredients)}}!</h1>
    <p>How are you?</p>
%end
</html>
