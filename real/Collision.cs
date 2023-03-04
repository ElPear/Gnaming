        private static bool Colliding(Control item1, Control item2)
        {
            if (item1.Location.X + item1.Width < item2.Location.X)
                return false;
            if (item2.Location.X + item2.Width < item1.Location.X)
                return false;
            if (item1.Location.Y + item1.Height < item2.Location.Y)
                return false;
            if (item2.Location.Y + item2.Height < item1.Location.Y)
                return false;
            return true;
        }
