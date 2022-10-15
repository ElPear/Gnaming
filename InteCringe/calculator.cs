string lableText = "";

private void OnClick(object sender, EventArgs e)
{
    var text = (Button)sender;
    lableText = lableText + text.Text;
    label.Text = lableText;
}
private void Calculate(object sender, EventArgs e)
{
    if (lableText != "9 + 10")
    {
        DataTable data = new DataTable();
        var equation = data.Compute(lableText, "");
        lableText = lableText + " = " + Math.Round(decimal.Parse(equation.ToString()), 3).ToString().Replace(",",".");
        label.Text = lableText;
        lableText = "";
    }
    else
    {
        label.Text = "9 + 10 = 21";
        lableText = "";
    }
}

private void Clear(object sender, EventArgs e)
{
    lableText = "";
    label.Text = lableText;
}A
