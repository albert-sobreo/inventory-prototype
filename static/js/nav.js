class Nav{
    template = `<div class="justify-content-center navbar">
                <div class="mx-3" id="nav-purchase" onclick="location.href='/in'">Purchase</div>
                <div class="mx-3" id="nav-sales" onclick="location.href='/out'">Sales</div>
                <div class="mx-3" id="nav-transfer" onclick="location.href='/transfer'">Transfer</div>
                <div class="mx-3" id="nav-spoilage" onclick="location.href='/spoilage'">Spoilage</div>
                <div class="mx-3" id="nav-vendors" onclick="location.href='/vendor'">Vendors</div>
                <div class="mx-3" id="nav-inventory" onclick="location.href='/inventory-page'">Inventory</div>
                <div class="mx-3" id="nav-warehouse" onclick="location.href='/'">Warehouse</div>
                <div class="mx-3" id="nav-reports" onclick="location.href='/reports/costofgoodsold'">Reports</div>
                <div class="mx-3" id="nav-logs" onclick="location.href='/logs/in'">Logs</div>
                <div class="mx-3" id="nav-customers" onclick="location.href='/customer'">Customers</div>
                <div class="btn-group mx-3">
                    <span id="nav-approvals" class="" data-toggle="dropdown">Approvals</span>
                    <div class="dropdown-menu b-radius-5 py-0">
                        <a href="/purchase/notapproved" class="dropdown-item font-size-12 font-w-600">Purchase</a>
                        <a href="/sales/notapproved" class="dropdown-item font-size-12 font-w-600">Sales</a>
                        <a href="/transfer/notapproved" class="dropdown-item font-size-12 font-w-600">Transfer</a>
                        <a href="/spoilage/notapproved" class="dropdown-item font-size-12 font-w-600">Spoilage</a> 
                    </div>
                </div>
                </div>`
    
    constructor(active){
        document.write(this.template)
        var element = document.getElementById(active)
        element.classList.add('active')
    }
}

class NavN{
    template = `<div class="c-nav-item justify-content-end dropdown">
                    <div class="nav-name" data-toggle="dropdown">
                        <i class="fas fa-user"></i> <i class="fas fa-angle-down ml-1"></i>
                    </div>
                    <div class="dropdown-menu dropdown-menu-left b-radius-5 py-0">
                      <div class="dropdown-header font-size-12">
                          <span id="name1"></span><br>
                          <span id="branch" class="font-size-10 py-0"></span><br>
                          <span id="position" class="font-size-10 py-0"></span>
                      </div>
                      <div class="dropdown-divider"></div>
                      <a href="/logout" class="dropdown-item font-size-12">Logout</a>
                    </div>
                </div>`

    constructor(fname, lname, branch, position){
        document.write(this.template)
        document.getElementById('name1').innerHTML = fname + " " + lname
        document.getElementById('branch').innerHTML = branch
        document.getElementById('position').innerHTML = position
    }
}

class NavN2{
    template = `<div class="c2-nav-item justify-content-end dropdown">
                    <div class="nav-name" data-toggle="dropdown">
                        <i class="fas fa-user"></i> <i class="fas fa-angle-down ml-1"></i>
                    </div>
                    <div class="dropdown-menu dropdown-menu-left b-radius-5 py-0">
                      <div class="dropdown-header font-size-12">
                          <span id="name1"></span><br>
                          <span id="branch" class="font-size-10 py-0"></span><br>
                          <span id="position" class="font-size-10 py-0"></span>
                      </div>
                      <div class="dropdown-divider"></div>
                      <a href="/logout" class="dropdown-item font-size-12">Logout</a>
                    </div>
                </div>`

    constructor(fname, lname, branch, position){
        document.write(this.template)
        document.getElementById('name1').innerHTML = fname + " " + lname
        document.getElementById('branch').innerHTML = branch
        document.getElementById('position').innerHTML = position
    }
}

class NavBC2{
    template = `<div class="justify-content-center navbar2">
                  <div class="mx-3" id="inventory" onclick="location.href='/top-level/branch/$branch$/inventory/'">Inventory</div>
                  <div class="mx-3" id="warehouse" onclick="location.href='/top-level/branch/$branch$/warehouse/'">Warehouse</div>
                  <div class="mx-3" id="logs" onclick="location.href='/top-level/branch/$branch$/logs/purchase/'">Logs</div>
                  <div class="mx-3" id="reports" onclick="location.href='/top-level/branch/$branch$/reports/costofgoodsold/'">Reports</div>
                </div>`

    constructor(active, pk_branch){
        document.write(this.template.replaceAll("$branch$", pk_branch))
        var element = document.getElementById(active)
        element.classList.add('active')
    }
}

class NavLogsTL{
    template = `<div class="d-flex font-w-600 mb-2 justify-content-center">
                    <div class="justify-content-center c-nav-links">
                        <div id="purchase" onclick="location.href='/top-level/branch/$branch$/logs/purchase'">Purchase</div>
                        <div id="sales" onclick="location.href='/top-level/branch/$branch$/logs/sales'">Sales</div>
                        <div id="transfers" onclick="location.href='/top-level/branch/$branch$/logs/transfers'">Transfer</div>
                        <div id="spoilage" onclick="location.href='/top-level/branch/$branch$/logs/spoilage'">Spoilage</div>
                    </div>
                </div> `

    constructor(active, pk_branch){
        document.write(this.template.replaceAll("$branch$", pk_branch))
        var element = document.getElementById(active)
        element.classList.add('active')
    }
}

class NavReportsTL{
    template = `<div class="d-flex font-w-600 mb-2 justify-content-center">
                    <div class="justify-content-center c-nav-links">
                    <div id="costofgoodsold" onclick="location.href='/top-level/branch/$branch$/reports/costofgoodsold'">Cost of Goods Sold</div>
                    </div>
                </div> `

    constructor(active, pk_branch){
        document.write(this.template.replaceAll("$branch$", pk_branch))
        var element = document.getElementById(active)
        element.classList.add('active')
    }
}