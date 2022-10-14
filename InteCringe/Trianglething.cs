private void Calculate()
        {
            int decimals=1;
            if (Decimalbox.Text != String.Empty)
            {
                decimals = int.Parse(Decimalbox.Text);
            }
            if (Xbox.Checked && Ybox.Checked)
            {
                Hypbox.Enabled = !true;
                Anglebox.Enabled = !true;
                
                if (Xkomp.Text != String.Empty && Ykomp.Text != String.Empty)
                {
                    double Ykomposant = double.Parse(Ykomp.Text);
                    double Xkomposant = double.Parse(Xkomp.Text);
                    double angle = Math.Atan(Ykomposant / Xkomposant) * (180 / Math.PI);
                    double Hypothenuse = Math.Sqrt(Math.Pow(Ykomposant, 2) + Math.Pow(Xkomposant, 2));

                    HypothenuseBox.Text = Math.Round(Hypothenuse, decimals).ToString();
                    Angle.Text = Math.Round(angle, decimals).ToString();
                }
                return;

            }

            if (Anglebox.Checked && Hypbox.Checked)
            {
                Xbox.Enabled = !true;
                Ybox.Enabled = !true;
                
                if (HypothenuseBox.Text != String.Empty && Angle.Text != String.Empty)
                {
                    double hypothenuse = double.Parse(HypothenuseBox.Text);
                    double angle = double.Parse(Angle.Text);
                    double Ykomposant = hypothenuse * Math.Sin(angle * (Math.PI / 180));
                    double Xkomposant = hypothenuse * Math.Cos(angle * (Math.PI / 180));

                    Ykomp.Text = Math.Round(Ykomposant, decimals).ToString();
                    Xkomp.Text = Math.Round(Xkomposant, decimals).ToString();
                }
                return;

            }

            if (Xbox.Checked && Hypbox.Checked)
            {
                Ybox.Enabled = !true;
                Anglebox.Enabled = !true;

                if (HypothenuseBox.Text != String.Empty && Xkomp.Text != String.Empty)
                {
                    double hypothenuse = double.Parse(HypothenuseBox.Text);
                    double Xkomposant = double.Parse(Xkomp.Text);
                    double Ykomposant = Math.Sqrt(Math.Pow(hypothenuse, 2) - Math.Pow(Xkomposant, 2));
                    double angle = Math.Atan(Ykomposant / Xkomposant) * (180 / Math.PI);

                    Angle.Text = Math.Round(angle, decimals).ToString();
                    Ykomp.Text = Math.Round(Ykomposant, decimals).ToString();
                }
                return;

            }

            if (Ybox.Checked && Hypbox.Checked)
            {
                Xbox.Enabled = !true;
                Anglebox.Enabled = !true;

                if (HypothenuseBox.Text != String.Empty && Ykomp.Text != String.Empty)
                {
                    double hypothenuse = double.Parse(HypothenuseBox.Text);
                    double Ykomposant = double.Parse(Ykomp.Text);
                    double Xkomposant = Math.Sqrt(Math.Pow(hypothenuse, 2) - Math.Pow(Ykomposant, 2));
                    double angle = Math.Atan(Ykomposant / Xkomposant) * (180 / Math.PI);

                    Angle.Text = Math.Round(angle, decimals).ToString();
                    Xkomp.Text = Math.Round(Xkomposant, decimals).ToString();
                }
                return;

            }

            if (Ybox.Checked && Anglebox.Checked)
            {
                Xbox.Enabled = !true;
                Hypbox.Enabled = !true;

                if (Angle.Text != String.Empty && Ykomp.Text != String.Empty)
                {

                    double Ykomposant = double.Parse(Ykomp.Text);
                    double angle = double.Parse(Angle.Text);
                    double Xkomposant = Ykomposant / Math.Tan(angle * (Math.PI / 180));
                    double hypothenuse = Math.Sqrt(Math.Pow(Ykomposant, 2) + Math.Pow(Xkomposant, 2));

                    HypothenuseBox.Text = Math.Round(hypothenuse, decimals).ToString();
                    Xkomp.Text = Math.Round(Xkomposant, decimals).ToString();
                }
                return;

            }

            if (Xbox.Checked && Anglebox.Checked)
            {
                Ybox.Enabled = !true;
                Hypbox.Enabled = !true;

                if (Angle.Text != String.Empty && Xkomp.Text != String.Empty)
                {
                    double Xkomposant = double.Parse(Xkomp.Text);
                    double angle = double.Parse(Angle.Text);
                    double Ykomposant = Xkomposant * Math.Tan(angle * (Math.PI / 180));
                    double hypothenuse = Math.Sqrt(Math.Pow(Ykomposant, 2) + Math.Pow(Xkomposant, 2));

                    HypothenuseBox.Text = Math.Round(hypothenuse, decimals).ToString();
                    Ykomp.Text = Math.Round(Ykomposant, decimals).ToString();
                    
                }
                return;

            }
            Xbox.Enabled = true;
            Ybox.Enabled = true;
            Hypbox.Enabled = true;
            Anglebox.Enabled = true;
        }
