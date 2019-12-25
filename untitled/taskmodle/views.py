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

    context['modal'] = """
    <!-- Button trigger modal -->
<!-- Modal -->
<div class="modal fade" id="staticBackdrop" data-backdrop="static" tabindex="-1" role="dialog" aria-labelledby="staticBackdropLabel" aria-hidden="true">
  <div class="modal-dialog" role="document">
    <div class="modal-content">
      <div class="modal-header">
        <h5 class="modal-title" id="staticBackdropLabel">添加目标任务</h5>
        <button type="button" class="close" data-dismiss="modal" aria-label="Close">
          <span aria-hidden="true">&times;</span>
        </button>
      </div>
      <div class="modal-body">
      
    <!-- 标题 -->
    <div class="input-group flex-nowrap">
      <div class="input-group-prepend">
        <span class="input-group-text" id="addon-wrapping">主题</span>
      </div>
      <input type="text" class="form-control" placeholder="Username" aria-label="Username" aria-describedby="addon-wrapping">
    </div>
    <p></p>
        
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
    <!-- 重要等级 -->
    <div class="input-group mb-3">
      <div class="input-group-prepend">
        <label class="input-group-text" for="inputGroupSelect01">重要等级</label>
      </div>
      <select class="custom-select" id="inputGroupSelect01">
        <option value="1">一般</option>
        <option value="2">重要</option>
        <option value="3">非常重要</option>
      </select>
    </div>
    <p></p>
    
    <!-- 完成时间 -->
    <div class="input-group flex-nowrap">
      <div class="input-group-prepend" >
        <span class="input-group-text" style="padding:.2rem .75rem;" id="addon-wrapping">完成时间</span>
        <wui-date 
            format="yyyy-mm-dd hh:mm" 
            placeholder="请选择或输入日期" 
            id="date3" 
            btns="{'ok':'确定','now':'此刻'}" 
            ng-model="date3"
        >
        </wui-date>
      </div>
    </div>
    <p></p>

       
    <!-- 详细内容 --> 
    <div class="form-group">
    <label for="exampleFormControlTextarea1">详细内容 ：</label>
    <textarea class="form-control" id="exampleFormControlTextarea1" rows="3"></textarea>
    </div>

      </div>
      <div class="modal-footer">
        <button type="button" class="btn btn-secondary" data-dismiss="modal">取消</button>
        <button type="button" class="btn btn-primary" data-dismiss="modal">添加</button>
        <input type="submit" class="btn btn-primary" value="添加" />
      </div>
    </div>
  </div>
</div>"""
    return render(request, 'test.html', context)
