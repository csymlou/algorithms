// 两个线程交替打印数字
package main

import (
	"fmt"
	"sync"
)

func main() {
	var lock1, lock2 sync.Mutex
	var n, m int = 1, 2
	var wg sync.WaitGroup
	wg.Add(2)

	lock2.Lock()

	go func() {
		for {
			lock1.Lock()
			for j := 0; j < 5; j++ {
				fmt.Println("1>>>", n)
				n += 2
				if n > 100 {
					lock2.Unlock()
					wg.Done()
					return
				}
			}
			lock2.Unlock()
		}
	}()

	go func() {
		for {
			lock2.Lock()
			for j := 0; j < 5; j++ {
				fmt.Println("2>>>", m)
				m += 2
				if m > 100 {
					lock1.Unlock()
					wg.Done()
					return
				}
			}
			lock1.Unlock()
		}
	}()

	wg.Wait()

}
