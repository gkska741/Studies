using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

/* 0~99사이 어떤 숫자일까요? 단, 0은 나가기 */
/* 이후 up & down진행, 정답 출력후 총 ~번 시도 출력*/
namespace _056_Check
{
    class Program
    {
        static void Main(string[] args)
        {
            Random rnd = new Random();
            int answer = rnd.Next(0, 100);
            int cnt = 0;
            while (true)
            {
                Console.Write("0~99 사이 어떤 숫자일까요(단, 0은 나가기)");
                int my_answer = int.Parse(Console.ReadLine());

                if (my_answer == 0)
                {
                    break;
                }

                if (my_answer == answer) 
                {
                    Console.WriteLine("== 정답입니다 ==");
                    break;
                }

                if (my_answer > answer)
                {
                    Console.WriteLine("입력한 수는 커요");
                    cnt += 1;
                }
                else
                {
                    Console.WriteLine("입력한 수는 작아요");
                    cnt += 1;
                }
            }
            Console.WriteLine("총 {0}번 시도하였습니다", cnt);
        }   
    }
}
