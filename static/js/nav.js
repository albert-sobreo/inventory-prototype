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
                    </div>
                </div>
                </div>`
    
    constructor(active){
        document.write(this.template)
        var element = document.getElementById(active)
        element.classList.add('active')
    }
}