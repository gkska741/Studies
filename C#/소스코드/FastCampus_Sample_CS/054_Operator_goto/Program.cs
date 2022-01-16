using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

/*-----------------------------------------------------------------------------
 * Name: _054_Operator_goto
 * DESC: goto 기초
-----------------------------------------------------------------------------*/
namespace _054_Operator_goto
{
    class Program
    {
        static void Main(string[] args)
        {
            for (int i = 0; i < 10; i++)
            {
                if(i == 5)
                {
                    goto AA;
                }

                if(i == 7)
                {
                    goto BB;
                }
                Console.WriteLine("i = {0}", i);

        
            }
        AA: Console.WriteLine("goto AA");

        BB: Console.WriteLine("goto BB");
        }
    }
}
