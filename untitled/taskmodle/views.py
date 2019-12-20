from django.shortcuts import render

# Create your views here.

def hello(request):
    context          = {}
    context['hello'] = ''

    context['Jumbotron'] = """<div class="jumbotron">
  <h1 class="display-4">Hello, world!</h1>
  <hr class="my-4">
  <p>It uses utility classes for typography and spacing to space content out within the larger container.</p>
  <button type="button" class="btn btn-primary" data-toggle="modal" data-target="#staticBackdrop">Add task</button>
</div>"""

    context['modal'] = """<!-- Button trigger modal -->


<!-- Modal -->
<div class="modal fade" id="staticBackdrop" data-backdrop="static" tabindex="-1" role="dialog" aria-labelledby="staticBackdropLabel" aria-hidden="true">
  <div class="modal-dialog" role="document">
    <div class="modal-content">
      <div class="modal-header">
        <h5 class="modal-title" id="staticBackdropLabel">Modal title</h5>
        <button type="button" class="close" data-dismiss="modal" aria-label="Close">
          <span aria-hidden="true">&times;</span>
        </button>
      </div>
      <div class="modal-body">
        
    <!-- 分类 -->
     <div class="input-group mb-3">
      <div class="input-group-prepend">
        <label class="input-group-text" for="inputGroupSelect01">分类</label>
      </div>
      <select class="custom-select" id="inputGroupSelect01">
        <option selected>Choose...</option>
        <option value="1">One</option>
        <option value="2">Two</option>
        <option value="3">Three</option>
      </select>
    </div>
    
    <!-- 完成时间 -->
<input type="text" class="form-control" value="02-16-2012">
<div class="input-group date">
    <input type="text" class="form-control" value="12-02-2012">
    <div class="input-group-addon">
        <span class="glyphicon glyphicon-th"></span>
    </div>
</div>
<div class="input-group input-daterange">
    <input type="text" class="form-control" value="2012-04-05">
    <div class="input-group-addon">to</div>
    <input type="text" class="form-control" value="2012-04-19">
</div>

    <!-- 标题 -->
    <div class="input-group flex-nowrap">
      <div class="input-group-prepend">
        <span class="input-group-text" id="addon-wrapping">主题</span>
      </div>
      <input type="text" class="form-control" placeholder="Username" aria-label="Username" aria-describedby="addon-wrapping">
    </div>
       
    <!-- 详细内容 --> 
    <div class="form-group">
    <label for="exampleFormControlTextarea1">详细内容 ：</label>
    <textarea class="form-control" id="exampleFormControlTextarea1" rows="3"></textarea>
    </div>

      </div>
      <div class="modal-footer">
        <button type="button" class="btn btn-secondary" data-dismiss="modal">Close</button>
        <button type="button" class="btn btn-primary">Understood</button>
      </div>
    </div>
  </div>
</div>"""
    return render(request, 'test.html', context)
